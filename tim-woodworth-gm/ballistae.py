#!/usr/bin/env python
import numpy as np
import argparse

def shoot(AC=15.,bShoot=11,bonus=2):
    attackRolls = np.random.randint(1,21,bShoot)+bonus

    print('Num Hit:',np.sum(attackRolls>=AC))
    print('AttackRolls:',attackRolls)
    print('Damage:     ',[np.sum(np.random.randint(1,9,2)) for x in range(bShoot)])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-ac', dest='ac',help='ac of enemy',required=True,type=float)
    parser.add_argument('-b', dest='b',required=True,help='number of ballistae',type=int)
    parser.add_argument('-v', dest='bonus',required=True,help='modifier for attack roll',type=float)


    args = parser.parse_args()
    shoot(args.ac,args.b,args.bonus)
