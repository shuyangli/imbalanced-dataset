import DS from 'ember-data';

export default DS.Model.extend({
  content: DS.attr('string'),
  precision_graph: DS.attr('string'),
  roc_graph: DS.attr('string'),
  image_url: Ember.computed('precision_graph', function() {
    return "http://localhost:8000" + this.get('precision_graph');
  }),
  roc_url: Ember.computed('roc_graph', function() {
    return "http://localhost:8000" + this.get('roc_graph');
  })
});
