import DS from 'ember-data';

export default DS.Model.extend({
  url: DS.attr('string'),
  name: DS.attr('string'),
  description: DS.attr('string'),
  data_file: DS.attr('string'),
  analyses: DS.hasMany('analysis')
});
