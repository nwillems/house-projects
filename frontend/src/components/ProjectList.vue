<template>
<table class="striped hoverable">
    <thead>
        <tr>
            <th>Title</th>
            <th>Deadline</th>
            <th>Description</th>
            <th>Budget</th>
            <th> # Proposals </th>
            <th></th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="project in projects" :key="project.id">
            <td>{{ project.title }}</td>
            <td>{{ project.deadline }}</td>
            <td>{{ project.description }}</td>
            <td>{{ project.budget }}</td>
            <td>{{ project.proposals.length }}</td>
            <td><router-link :to="{ name: 'ProjectDetail', params: { projectid: project.id }}">Open</router-link></td>
        </tr>
    </tbody>
</table>

</template>

<script>
export default {
  name: 'ProjectForm',
  props: ['projects']
}
</script>
