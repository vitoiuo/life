<template>
    <div>
        <label for="colsInpt">Colunas</label>
        <input id='colsInpt' type="number" v-model.number='numCols'>

        <label for="rowsInpt">Linhas</label>
        <input id='rowsInpt' type="number" v-model.number='numRows'>
        <div>
            <div v-for='r in numRows' :key='r'> 
                <life-cell :disabled='disableBoard' v-for="c in numCols" :key='r+c' @update-alive='updateCell($event,r-1,c-1)' :alive="matrice[r-1][c-1]"></life-cell>
            </div>
        </div>

        <button @click='init'>START</button>
    </div>
</template>

<script>
import lifeCell from './life-cell.vue' 

export default {
    components: {
        lifeCell
    },
    data() {
        return {
            numCols: 4,
            numRows: 4,
            disableBoard: false
        }
    },
    methods: {
        init() {
            // this.disableBoard = true
            this.matrice.forEach(row => {
                row.forEach((column,i) => {
                    //Casos:
                    // coluna 0 ou [-1]
                    // linha 0 ou [-1]
                    // resto é vapo?
                    console.log(column, i)
                })
            })
        },
        updateCell(newValue, r, c) {
            this.matrice[r][c] = newValue
            this.$forceUpdate();
        }
    },
    computed: {
        matrice() {
            return Array(this.numRows).fill(false).map(()=>Array(this.numCols).fill(false))
        }
    }, 
}
</script>
