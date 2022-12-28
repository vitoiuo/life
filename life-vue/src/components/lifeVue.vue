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
                <input id='speedInput' type="range"  min="100" max="2000" v-model.number='gameSpeed'>
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
                <button @click='init'>START</button>
                <button @click='stop = true'>STOP</button>
                <button @click='clear'>CLEAR</button>
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
            gameSpeed: 1000
        }
    },
    methods: {
        init() {
            this.stop = false
            const rotina = setInterval(() => {
                console.log('Madeiraaaa')
                const matrice_clone =  JSON.parse(JSON.stringify(this.matrice))

                Array.prototype.forEach.call(this.matrice, (row,ri) => {
                    row.forEach((_,ci) => {
                        let neighbourHood

                        if(ri === 0 && ci === 0) {
                            neighbourHood = this.matrice.slice(ri, ri+2).map(e => e.slice(ci, ci+2))
                        }
                        else if (ri === this.matrice.length-1 && ci === 0) {
                            neighbourHood = this.matrice.slice(ri-1, ri+1).map(e => e.slice(ci, ci+2))
                        }
                        else if (ri === 0 && ci === row.length-1) {
                            neighbourHood = this.matrice.slice(ri, ri+2).map(e => e.slice(ci-1, ci+1))
                        }
                        else if (ri === this.matrice.length-1 && ci === row.length-1) {
                            neighbourHood = this.matrice.slice(ri-1, ri+1).map(e => e.slice(ci-1, ci+1))
                        }
                        else if (ri === 0) {
                            neighbourHood = this.matrice.slice(ri, ri+2).map(e => e.slice(ci-1, ci+2))
                        }
                        else if (ri === this.matrice.length-1) {
                            neighbourHood = this.matrice.slice(ri-1, ri+1).map(e => e.slice(ci-1, ci+2))
                        }
                        else if (ci === 0) {
                            neighbourHood = this.matrice.slice(ri-1, ri+2).map(e => e.slice(ci, ci+2))
                        }
                        else if ((ci === row.length-1)) {
                            neighbourHood = this.matrice.slice(ri-1, ri+2).map(e => e.slice(ci-1, ci+1))
                        }
                        else {
                            neighbourHood = this.matrice.slice(ri-1, ri+2).map(e => e.slice(ci-1, ci+2))
                        }
                        neighbourHood = neighbourHood.flat();
                        let neighboursAlive = neighbourHood.filter(neighbour => neighbour === true).length

                        if (this.matrice[ri][ci]) {
                            neighboursAlive-=1
                            if ([2,3].includes(neighboursAlive)) {
                                matrice_clone[ri][ci] = true
                            }
                            else {
                                matrice_clone[ri][ci] = false
                            }
                        }
                        else if(neighboursAlive === 3) {
                            matrice_clone[ri][ci] = true
                        }
                    })
                 })
                this.matrice = JSON.parse(JSON.stringify(matrice_clone))

                if (!this.matrice.flat().some(e => e === true) || this.stop) clearInterval(rotina)
            }, this.gameSpeed)
        },
        clear () {
            this.matrice = Array(this.numRows).fill(false).map(()=>Array(this.numCols).fill(false))
        }
    },
    watch: {
        numCols(newValue) {
            this.matrice = Array(this.numRows).fill(false).map(()=>Array(newValue).fill(false))
        },
        numRows(newValue) {
           this.matrice = Array(newValue).fill(false).map(()=>Array(this.numCols).fill(false))
        }
    }
}
</script>

<style scoped>
.board {
    margin: 24px 0;
    text-align: center;
    align-items: ;
}
</style>