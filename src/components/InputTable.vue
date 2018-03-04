<template>
<div id="input-table">
  <table>
    <thead>
      <tr>
        <th>Nombre</th>
        <th>Estructura</th>
        <th>Valor numérico</th>
      </tr>
    </thead>
    <tbody>
      <input-command v-on:nameSet="nameSet" v-on:valueSet="valueSet" />
    </tbody>
  </table>
</div>
</template>

<script>
import InputCommand from '@/InputCommand.vue'

export default {
  name: 'InputTable',
  components: {
    InputCommand
  },
  methods: {
    nameSet: function (name, value) {
      this.$emit('valueSet', name, value)
    },
    valueSet: function (name, value) {
      this.$emit('valueSet', name, value)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
