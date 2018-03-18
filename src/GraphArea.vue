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
  methods: {
    drawTree: function (tree, x, y) {
      let rect = this.snap.rect(x, y, 100, 50)
      rect.attr({
        stroke: 'black',
        strokewidth: 5,
        fill: 'white'
      })
      this.snap.text(x + 100 / 2,
                     y + 50 / 2 + 10,
                     tree.label)
      if ('left' in tree) {
        this.drawTree(tree.left, x, y + 50 + 50)
      }

      if ('right' in tree) {
        this.drawTree(tree.right, x + 100 + 50, y)
      }
    }
  },
  watch: {
    expr: function (newRoot, oldRoot) {
      this.snap.clear()

      this.drawTree(newRoot, 10, 10)
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
