<template>
<div id="app">
    <div id="interpreter">
          <textarea v-model="expr" v-on:input="parseExpr"></textarea>
    </div>
    <input-table v-on:valueSet="valueSet" />
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
      this.inputTable[name] = value
      console.log('The input table', this.inputTable)
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
