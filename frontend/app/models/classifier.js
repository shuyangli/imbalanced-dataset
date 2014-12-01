import DS from 'ember-data';

export default DS.Model.extend({
  url: DS.attr('string'),
  name: DS.attr('string'),
  description: DS.attr('string'),
  program_file: DS.attr('string')
});
