import DjangoSerializer from './django';

export default DjangoSerializer.extend({
    serializeHasMany: function(record, json, relationship) {
    if (relationship.options.polymorphic) {
      // TODO implement once it's implemented in DS.JSONSerializer
      return;
    }

    var key = relationship.key,
    json_key = this.keyForRelationship(key, "hasMany"),
    //relationshipType = DS.RelationshipChange.determineRelationshipType(
      //record.constructor, relationship);
    relationshipType = record.constructor.determineRelationshipType(relationship);

      if (relationshipType === 'manyToNone' || relationshipType === 'manyToMany') {
        json[json_key] = record.get(key).mapBy('id');
      }
  },
});
