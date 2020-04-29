<template>
    <div>
    <form v-on:submit.prevent="">
        <fieldset>
            <legend>Proposal</legend>
            <div class="row responsive-label">
                <div class="col-sm-12 col-md-4"><label for="contractor">Contractor</label></div>
                <div class="col-sm-12 col-md"><input type="text" id="contractor" placeholder="Name" v-model="value.contractor" /></div>
            </div>
            <div class="row responsive-label">
                <div class="col-sm-12 col-md-4"><label for="contractor_email">Email</label></div>
                <div class="col-sm-12 col-md"><input type="text" id="contractor_email" placeholder="email" v-model="value.contractor_email" /></div>
            </div>

            <div class="row responsive-label">
                <div class="col-sm-12 col-md-4"><label for="contractor_response">Response</label></div>
                <div class="col-sm-12 col-md"><textarea id="contractor_response" v-model="value.contractor_response"></textarea></div>
            </div>

            <div class="row responsive-label">
                <div class="col-sm-12 col-md-4"><label for="offer">Offer</label></div>
                <div class="col-sm-12 col-md"><input type="text" id="offer" placeholder="100" v-model="value.offer" /></div>
            </div>

            <div class="col-sm-offset-9">
                <button v-on:click="$emit('input', value);$emit('save', value);">Save</button>
            </div>
        </fieldset>
    </form>
    </div>
</template>

<script>

export default {
  name: 'ProposalForm',
  props: {
    value: {}
  },
  components: {}
}
</script>
