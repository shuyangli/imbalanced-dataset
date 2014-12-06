import DS from 'ember-data';

export default DS.Model.extend({
  content: DS.attr('string'),
  precision_graph: DS.attr('string'),
  image_url: Ember.computed('precision_graph', function() {
    return "http://localhost:8000" + this.get('precision_graph');
  })
});
