<template>
<tr>
  <th>
    <input v-model="name" v-on:change="nameSet" type="text" name="name" />
  </th>
  <th>
    <input type="text" name="struct" />
  </th>
  <th>
    <input v-model="value" v-on:change="valueSet" type="text" name="value" />
  </th>
</tr>
</template>

<script>
export default {
  name: 'InputCommand',
  data: function () {
    return {
      name: '',
      value: null
    }
  },
  methods: {
    nameSet: function () {
      this.$emit('nameSet', this.name, this.value)
      console.log('new name', this.name)
    },
    valueSet: function () {
      this.$emit('valueSet', this.name, this.value)
      console.log('new value', this.value)
    }
  }

}
</script>

<style scoped>
</style>
