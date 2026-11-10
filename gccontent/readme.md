- early strategies to analyze language was the frequency of which letter appeared in text
- that can be applied to biology: although two members of the same species will have different genomes, they still share the vast percentage of their DNA
- for this reason, biologists will speak of the human genome, meaning an average case genome derived from a collection of individuals. This means that such an average case genome can be assembled for any species. 

- the biological analog of identifying unknown text arises when researchers encouter a molecule of DNA from an unknown species. Because of the base pair relations of the two DNA strands, cytosine and guanine will always appear in equal amounts in a double standed DNA molecule. Thus, to analyze the symbol frequencies of DNA for comparison against a database, we compute the GC-content or the percentages of its bases that are EITHER cytosine or guanine

- in practice, the gc-content of most eukaryotic genomics hover around 50%. however, because genomes are so long, we may be able to distinguish species based on very small discrepancies in GC-content; furthermore, most prokaryotes have GC-content significantly higher then 50% so that GC-content can be used ot quickly differentiate most prokaryotes and eukaryotes by using relatively small DNA samples. 

Problem

Given at most DNA strings in FASTA format (of length at most 1 kbp each), return the ID of the string having teh highest GC-content followed by the GC-content of the string. 