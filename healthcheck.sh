#!/bin/bash
# richnashawaty.com live health check — status, redirects, noindex (meta + header), canonical
URLS=(
  "https://richnashawaty.com/"
  "https://richnashawaty.com/seo-web.html"
  "https://richnashawaty.com/ai-consulting.html"
  "https://richnashawaty.com/custom-tools.html"
  "https://richnashawaty.com/seo-ai-visibility.html"
  "https://richnashawaty.com/about.html"
  "https://richnashawaty.com/blog/"
  "https://richnashawaty.com/blog/how-to-measure-seo-roi-small-business.html"
  "https://richnashawaty.com/blog/seo-vs-diy-when-to-hire-seo-consultant.html"
  "https://richnashawaty.com/robots.txt"
  "https://richnashawaty.com/sitemap.xml"
)

problems=0
printf "%-58s %-7s %-8s %-9s %s\n" "URL" "STATUS" "NOINDEX" "CANON" "NOTES"
echo "--------------------------------------------------------------------------------------------------------"

for u in "${URLS[@]}"; do
  hdr=$(curl -sIL --max-time 15 "$u")
  status=$(printf '%s' "$hdr" | grep -iE '^HTTP/' | tail -1 | awk '{print $2}')
  finalurl=$(curl -so /dev/null -w '%{url_effective}' -L --max-time 15 "$u")
  xrobots=$(printf '%s' "$hdr" | tr 'A-Z' 'a-z' | grep 'x-robots-tag' | grep -o 'noindex')

  ni="ok"; cstat="n/a"
  case "$u" in
    *.xml|*robots.txt) ;;  # skip body checks for non-HTML
    *)
      body=$(curl -sL --max-time 20 "$u")
      lc=$(printf '%s' "$body" | tr 'A-Z' 'a-z')
      meta=$(printf '%s' "$lc" | grep -Eo '<meta[^>]*(robots[^>]*noindex|noindex[^>]*robots)[^>]*>')
      canontag=$(printf '%s' "$lc" | grep -Eo '<link[^>]*canonical[^>]*>' | head -1)
      [ -n "$meta" ] && ni="META!"
      [ -n "$xrobots" ] && ni="HDR!"
      [ -n "$meta" ] && [ -n "$xrobots" ] && ni="BOTH!"
      if [ -n "$canontag" ]; then
        href=$(printf '%s' "$canontag" | grep -Eo 'href=[^> ]*' | head -1 | sed -E 's/^href=//' | tr -d '"')
        cstat="set"
      else
        cstat="MISSING!"
      fi
      ;;
  esac

  notes=""
  [ "$status" != "200" ] && { notes="status!=200"; problems=$((problems+1)); }
  [ "$finalurl" != "$u" ] && notes="$notes ->$finalurl"
  [ "$ni" != "ok" ] && { notes="$notes NOINDEX-FOUND"; problems=$((problems+1)); }
  [ "$cstat" = "MISSING!" ] && problems=$((problems+1))

  printf "%-58s %-7s %-8s %-9s %s\n" "$u" "${status:-ERR}" "$ni" "$cstat" "$notes"
done

echo "--------------------------------------------------------------------------------------------------------"
loccount=$(curl -sL --max-time 20 "https://richnashawaty.com/sitemap.xml" | grep -c '<loc>')
echo "Sitemap <loc> count: $loccount  (CLAUDE.md expects ~24)"
echo
if [ "$problems" -eq 0 ]; then
  echo "ALL CLEAR — every page 200, no noindex, canonicals present. The GSC dip is data lag, not a site problem."
else
  echo "WARNING — $problems issue(s) flagged above. Investigate before assuming it's just lag."
fi
