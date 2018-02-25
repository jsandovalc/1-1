<template>
  <div id="app">
    <div id="input">
          <textarea v-model="expr" v-on:input="parseExpr"></textarea>
    </div>
    <div id="output">
      <table>
        <thead>
          <tr>
            <th>A</th>
            <th>B</th>
            <th>C</th>
          </tr>
        </thead>
        <tbody>
          <th></th>
          <th></th>
          <th></th>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data: function () {
    return {
      expr: ''
    }
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
