<template>
  <div>
    <div class="btn btn-primary col-12 row mb-1" data-toggle="collapse" v-bind:data-target="'#'+unique_id" aria-expanded="true" aria-controls="collapseExample">
      {{ first_name }} {{ last_name }}
    </div>
    <div class="collapse show row mb-4" v-bind:id="unique_id">
      <div class="card card-body">
        Prefix: {{ prefix }} <br>
        First Name: {{ first_name }} <br>
        Middle Name: {{ middle_name }} <br>
        Last Name: {{ last_name }} <br>
        Suffix: {{ suffix }} <br>
        Address: {{ address }} <br>
        Mailing Address: {{ mailing_address }} <br>
        Birth date: {{ birth_date }} <br>
        Is Prospect: {{ is_prospect }} <br>
        <a v-bind:href="'/get-person/'+unique_id">
          GOTO
        </a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Collapsible Person',
  props: ['unique_id'],
  data () {
    return {
      uniqueId: '',
      prefix: '',
      firstName: '',
      middleName: '',
      lastName: '',
      suffix: '',
      address: '',
      mailingAddress: '',
      birthDate: '',
      customerType: '',
      height: '',
      weight: '',
      socialSecurityNumber: null,
      canUseCreditScore: false
    }
  },
  methods: {
    load (id) {
      fetch('http://localhost:5000/api/person/' + id)
        .then(response => response.json())
        .then(response => {
          console.log(response)
          this.prefix = response.prefix
          this.firstName = response.first_name
          this.middleName = response.middle_name
          this.lastName = response.last_name
          this.suffix = response.suffix
          this.address = response.address
          this.mailingAddress = response.mailing_address
          this.birthDate = response.birth_date
          this.customerType = response.customer_type
          this.height = response.height
          this.weight = response.weight
          this.socialSecurityNumber = response.social_security_number
          this.canUseCreditScore = response.can_use_credit_score
        })
    }
  }
}
</script>

<style scoped>

</style>
