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
  props: ['expr'],
  mounted: function () {
    var snap = Snap('#svg')
    this.snap = snap
  },
  watch: {
    expr: function (newExpr, oldExpr) {
      // must clear canvas. Redraw on new expression.
      this.snap.clear()
      let self = this

      let x = 10
      let y = 10
      let width = 100
      let height = 50

      newExpr.forEach(function (value, index) {
        let rect = self.snap.rect(x, y, width, height)
        rect.attr({
          stroke: 'black',
          strokewidth: 5,
          fill: 'white'})

        self.snap.text((x + width) / 2,
                       (y + height) / 2 + 10,
                       value.label)
      })
    }
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
