import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr('string'),
  description: DS.attr('string'),
  data_file: DS.attr('string'),
  analyses: DS.hasMany('analysis'),
  has_headers: DS.attr('boolean'),
  pos_label: DS.attr('number')
});
