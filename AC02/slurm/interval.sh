#!/bin/bash
#SBATCH --job-name=primes_job_rjhs
#SBATCH -t 0-2:00                               # time (D-HH:MM)
#SBATCH -o slurm-%a.out                         # STDOUT
#SBATCH -e slurm-%a.err                         # STDERR
#SBATCH --mail-type=END,FAIL                    # notifications for job done & fail
#SBATCH --mail-user=user@gmail.com              # send-to address
#SBATCH --workdir=/user/rjherrera/slurm/results   #cambiar esto /user/<algo>/slurm
#
#SBATCH --ntasks 1
#SBATCH --array 0-100%100                        # 100 procesos, 10 simultáneos

srun python3 ../primes.py $SLURM_ARRAY_TASK_ID

