<template>
  <button :class='{"box":true, "alive":alive}' @click="changeState"></button>
</template>

<script>
export default {
    props: {
      alive: {
        type: Boolean,
        default: false,
      }
    },
    methods: {
        changeState () {
            this.$emit('update:alive', !this.alive)
        }, 
    }
}
</script>

<style>
.box {
    display: inline-block;
    border: 1px solid gray;
    padding: 12px;
    color: white;
    background-color: black;
}
.alive {
    color: black;
    background-color: white;
}

@media (min-width: 1200px)
{
  .box {
    padding: 16px;
  }
}
</style>