<template>
<svg id="svg">

</svg>
</template>

<script>
import Snap from 'snapsvg'

export default {
  name: 'InputCommand',
  data: function () {
    return {
      snap: null
    }
  },
  mounted: function () {
    var snap = Snap('#svg')
    this.snap = snap
  }
}
</script>

<style scoped>
svg {
  width: 300px;
  height: 300px;
  border-radius: 10px;
  border: solid 2px #ccc
}
</style>
