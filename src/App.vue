<template>
<div id="app">
    <div id="interpreter">
      <textarea v-model="expr" v-on:input="parseExpr"></textarea>
    </div>
    <div id="input-table">
      <input-table v-on:valueSet="valueSet" v-on:exprSet="exprSet" />
    </div>
    <div  id="graph-area">
      <graph-area :expr="visExpr" />
    </div>
</div>
</template>

<script>
import axios from 'axios'
import InputTable from '@/components/InputTable.vue'
import GraphArea from '@/GraphArea.vue'

export default {
  name: 'App',
  data: function () {
    return {
      expr: '',
      visExpr: [],
      inputTable: {}
    }
  },
  components: {
    InputTable,
    GraphArea
  },
  methods: {
    parseExpr: function () {
      axios.post('/parse', {
        expr: '1 + 1'
      }).then(function (response) {
        console.log(response)
      }).catch(function (error) {
        console.log(error)
      })
    },

    valueSet: function (name, value) {
      this.expr += '\n=> ' + name + ' = ' + value
      this.inputTable[name] = Number(value)
      console.log('The input table', this.inputTable)
    },

    exprSet: function (expr, row) {
      var self = this

      // Update graph area
      axios.post('/display', {
        expr: expr
      }).then(function (response) {
        self.visExpr = response.data
      }).catch(function (error) {
        console.log('error', error)
      })

      // get the result
      axios.post('/eval', {
        expr: expr,
        table: this.inputTable
      }).then(function (response) {
        row.value = response.data.result
      }).catch(function (error) {
        console.log(error)
      })
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
