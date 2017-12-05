

def cat_json(output_filename, input_filenames):
    with open(output_filename, "w") as outfile:
        first = True
        for infile_name in input_filenames:
            with open(infile_name) as infile:
                if first:
                    outfile.write('[')
                    first = False
                else:
                    outfile.write(',')
                t = infile.read().strip('[')
                t.strip(']')
                outfile.write(t)
        outfile.write(']')

cat_json("mergedv2.json", ['output_asos.json', 'output_zalando.json', 'output_zappos.json', 'output_zumiez.json'])

