<template>
    <div>
    <form v-on:submit.prevent="">
        <fieldset>
            <legend>Project</legend>
            <div class="row responsive-label">
                <div class="col-sm-12 col-md-3"><label for="title">Title</label></div>
                <div class="col-sm-12 col-md"><input type="text" id="name" placeholder="Name" v-model="value.title" /></div>
            </div>

            <div class="row responsive-label">
                <div class="col-sm-12 col-md-3"><label for="budget">Budget</label></div>
                <div class="col-sm-12 col-md"><input type="number" id="budget" placeholder="Budget" v-model="value.budget" /></div>
            </div>

            <div class="row responsive-label">
                <div class="col-sm-12 col-md-3"><label for="deadline">Deadline</label></div>
                <div class="col-sm-12 col-md"><input type="date" id="deadline" placeholder="Deadline" v-model="value.deadline" /></div>
            </div>

            <div class="row responsive-label">
                <div class="col-sm-12 col-md-3"><label for="description">Description</label></div>
                <div class="col-sm-12 col-md"><textarea id="description" placeholder="Description" v-model="value.description"></textarea></div>
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
  name: 'ProjectForm',
  props: {
    value: {}
  },
  components: {}
}
</script>
