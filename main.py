import numpy as np
import matplotlib.pylab as plt

U = 8
D = 5
L = 4
R = 6

class state:
    
    mat = None
    freePos = 0
    
    def __init__(self,wh):
        self.mat = np.zeros((wh,wh),dtype=np.int32)
        self.freePos = self.mat.shape[0]*self.mat.shape[1]
        return None
    
    def getState(self):
        return self.mat

    def count_free_pos(self):
        c = self.mat.shape[0]*self.mat.shape[1] - np.count_nonzero(self.mat)
        if c == 0:
            print("-----------------")
            print("----GAME OVER----")
            print("-----------------")
        return c
    
    def create_new_tile(self):
        r = np.random.randint(2)
        if r == 0:
            c = 2
        else:
            c = 4
        if self.count_free_pos():
            p = np.random.randint(self.mat.shape[0], size=(1, 2))
            while self.mat[p[0][0]][p[0][1]] > 0:
                p = np.random.randint(self.mat.shape[0], size=(1, 2))
            self.mat[p[0][0]][p[0][1]] = c
        else:
            print("Game Over")
        return
    
    def move_tiles(self,d,verbose=False):
        didMove = False
        didWin = False
        try:
            d = int(d)
        except:
            return didMove, not didWin
        
        if d == U:
            for c in range(self.mat.shape[0]):
                v = np.zeros(self.mat.shape[0],dtype=np.int32)
                for r in range(self.mat.shape[0]):
                    v[r] = self.mat[r][c]
                if verbose:
                    print("v is",v)
                vb = v.copy()
                v = self.move(v,d)
                if not didWin:
                    didWin = self.did_win(v)
                if not np.array_equal(v,vb) and np.sum(v) > 0 and not didMove:
                    #print("vb",vb)
                    #print("v",v)
                    #print("didMove",didMove)
                    didMove = True
                for r in range(self.mat.shape[0]):
                    self.mat[r][c] = v[r]
        elif d == D:
            for c in range(self.mat.shape[0]):
                v = np.zeros(self.mat.shape[0],dtype=np.int32)
                for r in range(self.mat.shape[0]):
                    v[r] = self.mat[r][c]
                if verbose:
                    print("v is",v)
                vb = v.copy()
                v = self.move(v,d)
                if not didWin:
                    didWin = self.did_win(v)
                if not np.array_equal(v,vb) and np.sum(v) > 0 and not didMove:
                    #print("vb",vb)
                    #print("v",v)
                    #print("didMove",didMove)
                    didMove = True
                for r in range(self.mat.shape[0]):
                    self.mat[r][c] = v[r]
        elif d == L:
            for c in range(self.mat.shape[0]):
                v = np.zeros(self.mat.shape[0],dtype=np.int32)
                for r in range(self.mat.shape[0]):
                    v[r] = self.mat[c][r] # reverse cr
                if verbose:
                    print("v is",v)
                vb = v.copy()
                v = self.move(v,d)
                if not didWin:
                    didWin = self.did_win(v)
                if not np.array_equal(v,vb) and np.sum(v) > 0 and not didMove:
                    #print("vb",vb)
                    #print("v",v)
                    #print("didMove",didMove)
                    didMove = True
                for r in range(self.mat.shape[0]):
                    self.mat[c][r] = v[r] # reverse cr
        elif d == R:
            for c in range(self.mat.shape[0]):
                v = np.zeros(self.mat.shape[0],dtype=np.int32)
                for r in range(self.mat.shape[0]):
                    v[r] = self.mat[c][r] # reverse cr
                if verbose:
                    print("v is",v)
                vb = v.copy()
                v = self.move(v,d)
                if not didWin:
                    didWin = self.did_win(v)
                if not np.array_equal(v,vb) and np.sum(v) > 0 and not didMove:
                    #print("vb",vb)
                    #print("v",v)
                    #print("didMove",didMove)
                    didMove = True
                for r in range(self.mat.shape[0]):
                    self.mat[c][r] = v[r] # reverse cr
        else:
            pass
        
        #print("didMove: ",didMove)
        if didWin:
            print(self.getState())
            print("-----------------")
            print("---- YOU WIN ----")
            print("-----------------")
        return didMove, not didWin
    
    def move(self,v,d,verbose=False):
        tmp = []
        for i in range(v.shape[0]):
            if v[i] > 0:
                tmp.append(v[i])
        
        if d == D or d == R:
            tmp[:] = tmp[::-1]
        
        for i in range(1,len(tmp)):
            if tmp[i] == tmp[i-1]:
                tmp[i-1] = tmp[i]*2
                tmp[i] = 0
          
        if verbose:
            print("TMP a",tmp)
        tmp[:] = [x for x in tmp if x is not 0]
        if verbose:
            print("TMP b",tmp)
        
        if verbose:
            print("b",v)
        
        v = np.zeros_like(v)
        if d == U:
            for i in range(len(tmp)):
                v[i] = tmp[i]
        elif d == D:
            for i in range(len(tmp)):
                v[i] = tmp[i]
            v = np.flip(v,0)
        elif d == L:
            for i in range(len(tmp)):
                v[i] = tmp[i]
            pass
        elif d == R:
            for i in range(len(tmp)):
                v[i] = tmp[i]
            v = np.flip(v,0)
        else:
            pass
        if verbose:    
            print("a",v)
        return v
    
    def did_win(self,v):
        #print("v",v)
        won = np.isin(2048,v)
        #print("won",won)
        return won

def disp(m):
    fig, ax = plt.subplots()
    ax.matshow(m,cmap=plt.get_cmap('Set3'))
    for i in range(m.shape[0]):
        for j in range(m.shape[0]):
            c = m[j,i]
            if c > 0:
                ax.text(i, j, str(c), va='center', ha='center',color='black')
                
    plt.rc('font', size=30)
    plt.axis('off')
    #ax.set_axis_off()
    fig.set_size_inches(3, 3)
    plt.show()
    
if __name__ == "__main__":
    still_playing = True
    did_move_tile = True
    game = state(4)
    while game.count_free_pos() and still_playing:
        print("------------------")
        if did_move_tile:
            game.create_new_tile()
        print(game.getState())
        disp(game.getState())
        m = input("Input: ")
        did_move_tile, still_playing = game.move_tiles(m)
        still_playing = False

