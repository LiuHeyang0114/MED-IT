import argparse
import re


parser = argparse.ArgumentParser(description='biasing words selection')
parser.add_argument('--biasing_list', type=str,
                    help='biasing list')
parser.add_argument('--in_path', type=str,
                    help='read in text path')
parser.add_argument('--out_path', type=str,
                    help='write out text path')
args = parser.parse_args()

rf1=open(args.in_path+'/hyp.trn')
wf1=open(args.out_path+'/hyp.trn','w')
rf2=open(args.in_path+'/ref.trn')
wf2=open(args.out_path+'/ref.trn','w')
bl=open(args.biasing_list)

biasing_list=[]
for line in bl.readlines():
    biasing_list.append(line.replace('\n',''))
bl.close()


for line in rf1.readlines():
    line_w=re.split(r'[()]',line.replace('	',''))
    line_f=' '+re.split(r'[()]',line)[0].replace('	','')+' '
    words=line_w[0].split(' ')
    for ids in range(len(words)):
        if words[ids] not in biasing_list:
            line_f=line_f.replace(' '+words[ids]+' ',' ')
    wf1.write(line_f+' ('+line_w[1]+')'+'\n')
rf1.close()

for line in rf2.readlines():
    line_w=re.split(r'[()]',line.replace('	',''))
    line_f=' '+re.split(r'[()]',line)[0].replace('	','')+' '
    words=line_w[0].split(' ')
    for ids in range(len(words)):
        if words[ids] not in biasing_list:
            line_f=line_f.replace(' '+words[ids]+' ',' ')
    wf2.write(line_f+' ('+line_w[1]+')'+'\n')
rf1.close()
