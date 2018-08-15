<template>
  <div class="mb-1" v-if="person.unique_id">
    <div class="btn btn-primary col-12 row" data-toggle="collapse" v-bind:data-target="'#'+person.unique_id" aria-expanded="true" aria-controls="collapseExample">
      {{ person.first_name }} {{ person.last_name }}
    </div>
    <div class="collapse show row mb-4" v-bind:id="person.unique_id">
      <div class="card card-body">
        <div class="row ml-0">Prefix: <b v-if="person.prefix">{{ person.prefix }}</b></div>
        <div class="row ml-0">First Name: <b v-if="person.first_name">{{ person.first_name }}</b></div>
        <div class="row ml-0">Middle Name: <b v-if="person.middle_name">{{ person.middle_name }}</b></div>
        <div class="row ml-0">Last Name: <b v-if="person.last_name">{{ person.last_name }}</b></div>
        <div class="row ml-0">Suffix: <b v-if="person.suffix">{{ person.suffix }}</b></div>
        <div class="row ml-0">Address: <b v-if="person.address">{{ person.address }}</b></div>
        <div class="row ml-0">Mailing Address: <b v-if="person.mailing_address">{{ person.mailing_address }}</b></div>
        <div class="row ml-0">Birth date: <b v-if="person.birth_date">{{ person.birth_date }}</b></div>
        <div class="row ml-0">Is Prospect: <b v-if="person.customer_type">{{ person.customer_type }}</b></div>
        <router-link v-bind:to="'/modify-person/'+person.unique_id" class="row ml-0">
          GOTO
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CollapsiblePerson',
  props: ['person']
}
</script>

<style scoped>

</style>
