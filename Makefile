
JEKYLL_VERSION=3.8
SITE=${shell pwd}/docs

.PHONY:  slides

jstart:
	 docker run --rm --name aic_docs  --volume="${SITE}:/srv/jekyll" -p 3002:4000 -it jekyll/jekyll:${JEKYLL_VERSION} jekyll serve --watch --drafts

posts:
	./genposts.sh
