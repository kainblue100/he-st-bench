"""Clone official repositories. Does not start training and does not touch a GPU."""
import os
import subprocess

root = "/mnt/storage/bzhang/he-st-bench/repos"
os.makedirs(root, exist_ok=True)
repos = {
    "Hist2ST": "https://github.com/biomed-AI/Hist2ST.git",
    "THItoGene": "https://github.com/yrjia1015/THItoGene.git",
    "TCGN": "https://github.com/lugia-xiao/TCGN.git",
    "ST-Net": "https://github.com/bryanhe/ST-Net.git",
    "DeepSpaCE": "https://github.com/tmonjo/DeepSpaCE.git",
    "iStar": "https://github.com/daviddaiweizhang/istar.git",
    "HisToGene": "https://github.com/maxpmx/HisToGene.git",
    "GeneCodeR": "https://github.com/AskExplain/GeneCodeR.git",
    "BLEEP": "https://github.com/bowang-lab/BLEEP.git",
    "TRIPLEX": "https://github.com/NEXGEM/TRIPLEX.git",
    "BrST-Net": "https://github.com/Mamunur-20/BrSTNet.git",
    "STimage": "https://github.com/BiomedicalMachineLearning/STimage.git",
    "HEtoSGEBench": "https://github.com/SydneyBioX/HEtoSGEBench.git",
}
log = []
for name, url in repos.items():
    dest = os.path.join(root, name)
    if os.path.isdir(os.path.join(dest, ".git")):
        log.append(name + " already")
        continue
    proc = subprocess.run(
        ["git", "clone", "--depth", "1", url, dest],
        capture_output=True,
        text=True,
    )
    tail = (proc.stderr or proc.stdout or "").strip().splitlines()
    log.append(f"{name} exit={proc.returncode} {tail[-1] if tail else ''}")
print("\n".join(log))
