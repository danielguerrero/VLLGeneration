import os

# the prototype name of the production folder
prod_proto = "VLLs2LLPs_MVLL_{0}_MA_{1}"

### things to replace are
### TEMPLATEMVLL [mVLL]
### TEMPLATEMA [mA]

def change_cards(cardname, replacements):
    
    ## first make a backup copy
    bkpname = cardname + '.bak'
    os.system('mv %s %s' % (cardname, bkpname))

    # edit the file
    fin  = open(bkpname, 'r')
    fout = open(cardname, 'w')

    for line in fin:
        for key, rep in replacements.items():
            line = line.replace(key, rep)
        fout.write(line)

    fin.close()
    fout.close()

    ## delete the backup file
    os.system('rm %s' % bkpname)


def do_point(mvll, ma):
    # 1 - create the folder
    folder = prod_proto.format(mvll, ma)
    if os.path.isdir(folder):
        print " >> folder", folder, "already existing, forcing its deletion"
        os.system('rm -r %s' % folder)
    os.system('mkdir ' + folder)
    
    # 2 - copy the original files
    template_flrd = 'template'
    run_card      = 'run_card.dat'
    proc_card     = 'proc_card.dat'
    param_card    = 'param_card.dat'
    extramodels   = 'extramodels.dat'
    customizecard = 'customizecards.dat'

    to_copy = [run_card, proc_card, extramodels, customizecard]

    for tc in to_copy:
        os.system('cp %s/%s %s/%s_%s' % (template_flrd, tc, folder, folder, tc) )

    replacements = {
        'TEMPLATEMVLL' : str(mvll),
        'TEMPLATEMA' : str(ma),
    }

    # 3 - edit in place the cards
    change_cards('%s/%s_%s' % (folder, folder, customizecard), replacements)
    change_cards('%s/%s_%s' % (folder, folder, proc_card), replacements)


####################################################################################

## mvll, ma
points = [
    (100, 10),
#    (200, 10),
#    (300, 10),
#    (700, 10),
#    (1000, 10),    
]

for p in points:
    print '... generating', p
    do_point(*p)
