<template>
<svg id="svg" style="width: 300px; height: 300px; border-radius: 10px; border: solid 2px #ccc">

</svg>
</template>

<script>
import Snap from 'snapsvg'

export default {
  name: 'InputCommand',
  mounted: function () {
    var snap = Snap('#svg')
    snap.circle(150, 150, 100)
  }
}
</script>

<style scoped>
</style>
