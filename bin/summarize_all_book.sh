for x in ../data/*.txt; do echo $x; bash book_summary.sh $x Release; done > release.txt
for x in ../data/*.txt; do echo $x; bash book_summary.sh $x Author; done > authors.txt
