.PHONY: results all clean help settings

include config.mk

DATA=$(wildcard data/*.txt)
RESULTS=$(patsubst data/%.txt,results/%.csv,$(DATA))


## all : regenerate all results.
all : $(RESULTS) results/collated.csv img/collated.png

## results/%.csv : regenerate result for any book.
results/%.csv : data/%.txt $(COUNT)
	python $(COUNT) $< > $@

## results/collated.csv : collate all results.
results/collated.csv : $(RESULTS) $(COLLATE)
	python $(COLLATE) $(RESULTS) > $@

## results/collated.png: plot the collated results.
img/collated.png : results/collated.csv bin/plotparams.yml
	python $(PLOT) $< --outfile $@ --plotparams $(word 2,$^)

## clean : remove all generated files.
clean :
	rm -f results/*.csv

## settings : show variables' values.
settings :
	@echo COUNT: $(COUNT)
	@echo DATA: $(DATA)
	@echo RESULTS: $(RESULTS)
	@echo COLLATE: $(COLLATE)
	@echo PLOT: $(PLOT)

## help : show all commands.
help :
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' \
    | column -t -s ':'