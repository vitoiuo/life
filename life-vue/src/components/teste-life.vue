<template>
    <div>
        <label for="colsInpt">Colunas</label>
        <input id='colsInpt' type="number" v-model.number='numCols'>

        <label for="rowsInpt">Linhas</label>
        <input id='rowsInpt' type="number" v-model.number='numRows'>
        <div>
            <div v-for='r in numRows' :key='r'> 
                <life-cell
                    v-for="c in numCols" :key='r+c'
                    @update-alive='updateCell($event,r-1,c-1)'
                    :alive="matrice[r-1][c-1]">
                </life-cell>
            </div>
        </div>

        <button @click='init'>START</button>
        <button @click='stop = true'>STOP</button>
        <button @click='clear'>CLEAR</button>
    </div>
</template>

<script>
import lifeCell from './life-cell.vue' 

export default {
    components: {
        lifeCell
    },
    created () {
        const initialMatrice = Array(this.numRows).fill(false).map(()=>Array(this.numCols).fill(false))
        this.initMatrice(initialMatrice)
    },
    data() {
        return {
            numCols: 24,
            numRows: 24,
            matrice: undefined,
            stop: false
        }
    },
    methods: {
        initMatrice(matrice) {
            this.matrice = matrice
        },
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
                        const neighboursAlive = neighbourHood.filter(neighbour => neighbour === true).length

                        if(this.matrice[ri][ci]) {
                            switch (neighboursAlive-1) {
                                case 0:
                                    matrice_clone[ri][ci] = false
                                    break
                                case 1:
                                    matrice_clone[ri][ci] = false
                                    break
                                case 2:
                                    matrice_clone[ri][ci] = true
                                    break
                                case 3:
                                    matrice_clone[ri][ci] = true
                                    break
                                default:
                                    matrice_clone[ri][ci] = false
                                    break
                            }
                        }
                        else if(neighboursAlive === 3) {
                            matrice_clone[ri][ci] = true
                        }
                    })
                 })
                this.matrice = JSON.parse(JSON.stringify(matrice_clone))

                    if (!this.matrice.flat().some(e => e === true) || this.stop) clearInterval(rotina)
                }, 1000)
        },
        updateCell(newValue, r, c) {
            this.$set(this.matrice[r], c, newValue)
            this.$forceUpdate()
        },
        clear () {
            this.matrice = Array(this.numRows).fill(false).map(()=>Array(this.numCols).fill(false))
        }
    },
    watch: {
        numCols(newValue) {
            const newMatrice = Array(this.numRows).fill(false).map(()=>Array(newValue).fill(false))
            this.initMatrice(newMatrice)
        },
        numRows(newValue) {
            const newMatrice = Array(newValue).fill(false).map(()=>Array(this.numCols).fill(false))
            this.initMatrice(newMatrice)
        }
    }
}
</script>
