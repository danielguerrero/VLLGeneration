import os
import math
# the prototype name of the production folder
prod_proto = "VLLs2LLPs_MVLL_{0}_MA_{1}_CTAU_{2}"

### things to replace are
### TEMPLATEMVLL [mVLL]
### TEMPLATEMA [mA]
### TEMPLATEMA [mAwidth]

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


def do_point(mvll, ma, actau):
    print "The new ctau [mm]: ",actau
    #change from ctau [mm] to width [GeV]
    w = (1.973269E-16)/(float(actau)/1000)
    
    awidth = math.sqrt( (math.pi*w*mvll**2)/(ma**3)   )
   
    print "The new i5:", awidth

    # 1 - create the folder
    folder = prod_proto.format(mvll, ma, actau)
    if os.path.isdir(folder):
        print " >> folder", folder, "already existing, forcing its deletion"
        os.system('rm -r %s' % folder)
    os.system('mkdir ' + folder)
    
    # 2 - copy the original files
    template_flrd = 'template_ctau'
    run_card      = 'run_card.dat'
    proc_card     = 'proc_card.dat'
    param_card    = 'param_card.dat'
    extramodels   = 'extramodels.dat'
    customizecard = 'customizecards.dat'

    to_copy = [run_card, proc_card, extramodels, customizecard]

    for tc in to_copy:
        os.system('cp %s/%s %s/%s_%s' % (template_flrd, tc, folder, folder, tc) )

    replacements = {
        'TEMPLATEMVLL'   : str(mvll),
        'TEMPLATEMA'     : str(ma),
        'TEMPLATEACTAU'  : str(actau),
        'TEMPLATEAWIDTH' : str(awidth),
    }

    # 3 - edit in place the cards
    change_cards('%s/%s_%s' % (folder, folder, customizecard), replacements)
    change_cards('%s/%s_%s' % (folder, folder, proc_card), replacements)


####################################################################################

## mvll, ma
points = [
    (200, 2, 850),
    (200, 2, 85),
]

for p in points:
    print '... generating', p
    do_point(*p)
