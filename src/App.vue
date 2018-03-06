<template>
<div id="app">
    <div id="interpreter">
          <textarea v-model="expr" v-on:input="parseExpr"></textarea>
    </div>
    <input-table v-on:valueSet="valueSet" v-on:exprSet="exprSet" />
</template>

<script>
import axios from 'axios'
import InputTable from '@/components/InputTable.vue'

export default {
  name: 'App',
  data: function () {
    return {
      expr: '',
      inputTable: {}
    }
  },
  components: {
    InputTable
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
      axios.post('/eval', {
        expr: expr,
        table: this.inputTable
      }).then(function (response) {
        console.log(response)
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
