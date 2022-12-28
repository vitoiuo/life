<template>
    <div>
        <section style="margin-top: 16px; display: flex;flex-direction:column; align-items: center; gap: 16px">
            <div>
                <label for="colsInpt">Colunas</label>
                <input id='colsInpt' type="range" v-model.number='numCols'  min="1" max="50">
            </div>
            <div>
                <label for="rowsInpt">Linhas</label>
                <input id='rowsInpt' type="range" v-model.number='numRows'  min="1" max="50">
            </div>
            <div>
                <label for="rowsInpt">Intervalo</label>
                <input id='speedInput' type="range"  min="100" max="2000" v-model.number='gameSpeed' :disabled='gameRunning'>
            </div>
        </section>
        
        <div class='board'>
            <div v-for='r in numRows' :key='r'> 
                <life-cell
                    v-for="c in numCols" :key='r+c'
                    v-bind:alive.sync="matrice[r-1][c-1]">
                </life-cell>
            </div>
            <section style="margin-top: 16px; display: flex; justify-content: center; gap: 16px">
                <button @click='initGame'>START</button>
                <button @click='stop = true'>STOP</button>
                <button @click='clearBoard'>CLEAR</button>
            </section>
        </div>
    </div>
</template>

<script>
import lifeCell from './life-cell.vue' 

export default {
    components: {
        lifeCell
    },
    created () {
        this.matrice = Array(this.numRows).fill(false).map(()=>Array(this.numCols).fill(false))
    },
    data() {
        return {
            numCols: 12,
            numRows: 12,
            matrice: undefined,
            stop: false,
            gameRunning: false,
            gameSpeed: 1000
        }
    },
    methods: {
        initGame () {
            this.stop = false
            this.gameRunning = true
            const rotina = setInterval(() => {
                console.log('Madeiraaaa')
                const matrice_clone =  JSON.parse(JSON.stringify(this.matrice))

                Array.prototype.forEach.call(this.matrice, (row,ri) => {
                    row.forEach((_,ci) => {
                        let neighbourHood

                        const right = ci+2
                        const left = ci - 1
                        const bottom = ri + 2
                        const top = ri - 1
                        const center = {row: ri, col: ci}

                        if(center.row === 0 && center.col === 0) {
                            neighbourHood = this.matrice.slice(center.row, bottom).map(e => e.slice(center.col, right))
                        }
                        else if (center.row === this.matrice.length-1 && center.col === 0) {
                            neighbourHood = this.matrice.slice(top, center.row+1).map(e => e.slice(center.col, right))
                        }
                        else if (center.row === 0 && center.col === row.length-1) {
                            neighbourHood = this.matrice.slice(center.row, bottom).map(e => e.slice(left, center.col+1))
                        }
                        else if (center.row === this.matrice.length-1 && center.col === row.length-1) {
                            neighbourHood = this.matrice.slice(top, center.row+1).map(e => e.slice(left, center.col+1))
                        }
                        else if (center.row === 0) {
                            neighbourHood = this.matrice.slice(center.row, bottom).map(e => e.slice(left, right))
                        }
                        else if (center.row === this.matrice.length-1) {
                            neighbourHood = this.matrice.slice(top, center.row+1).map(e => e.slice(left, right))
                        }
                        else if (center.col === 0) {
                            neighbourHood = this.matrice.slice(top, bottom).map(e => e.slice(center.col, right))
                        }
                        else if ((center.col === row.length-1)) {
                            neighbourHood = this.matrice.slice(top, bottom).map(e => e.slice(left, center.col+1))
                        }
                        else {
                            neighbourHood = this.matrice.slice(top, bottom).map(e => e.slice(left, right))
                        }
                        neighbourHood = neighbourHood.flat();
                        let neighboursAlive = neighbourHood.filter(neighbour => neighbour === true).length

                        this.buildNewMatrice(matrice_clone, neighboursAlive, ri, ci)
                    })
                 })
                this.matrice = JSON.parse(JSON.stringify(matrice_clone))

                if (!this.matrice.flat().some(e => e === true) || this.stop){
                    clearInterval(rotina)
                    this.gameRunning = false
                } 
            }, this.gameSpeed)
        },
        buildNewMatrice (matrice_clone, neighboursAlive, row, col) {
            if (this.matrice[row][col]) {
                neighboursAlive-=1
                if ([2,3].includes(neighboursAlive)) {
                    matrice_clone[row][col] = true
                }
                else {
                    matrice_clone[row][col] = false
                }
            }
            else if(neighboursAlive === 3) {
                matrice_clone[row][col] = true
            }
        },
        clearBoard () {
            this.matrice = Array(this.numRows).fill(false).map(()=>Array(this.numCols).fill(false))
        },
    },
    watch: {
        numCols(newValue) {
            this.matrice = Array(this.numRows).fill(false).map(()=>Array(newValue).fill(false))
        },
        numRows(newValue) {
           this.matrice = Array(newValue).fill(false).map(()=>Array(this.numCols).fill(false))
        },
    }
}
</script>

<style scoped>
.board {
    margin: 24px 0;
    text-align: center;
}
</style>