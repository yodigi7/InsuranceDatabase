<template>
  <div v-if="message" v-bind:class="'alert alert-' + type+ ' alert-dismissible fade in show'">
    {{ message }}
    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
      <span aria-hidden="true">&times;</span>
    </button>
  </div>
</template>

<script>
export default {
  name: 'FlashMessage',
  props: ['message', 'type']
}
</script>

<style scoped>

</style>
