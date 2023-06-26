db.contacts.insertMany([{
  "_id": {
    "$oid": "6495ce1c16abbbed0d787930"
  },
  "name": "django_migrations",
  "auto": {
    "field_names": [
      "id"
    ],
    "seq": 27
  },
  "fields": {
    "app": {
      "type_code": "string"
    },
    "applied": {
      "type_code": "date"
    },
    "id": {
      "type_code": "long"
    },
    "name": {
      "type_code": "string"
    }
  }
},
{
  "_id": {
    "$oid": "6495ce1c16abbbed0d787935"
  },
  "name": "django_content_type",
  "auto": {
    "field_names": [
      "id"
    ],
    "seq": 9
  },
  "fields": {
    "app_label": {
      "type_code": "string"
    },
    "id": {
      "type_code": "int"
    },
    "model": {
      "type_code": "string"
    }
  }
},
{
  "_id": {
    "$oid": "6495ce1c16abbbed0d78793f"
  },
  "name": "auth_permission",
  "auto": {
    "field_names": [
      "id"
    ],
    "seq": 36
  },
  "fields": {
    "codename": {
      "type_code": "string"
    },
    "content_type_id": {
      "type_code": "int"
    },
    "id": {
      "type_code": "int"
    },
    "name": {
      "type_code": "string"
    }
  }
},
{
  "_id": {
    "$oid": "6495ce1c16abbbed0d787945"
  },
  "name": "auth_group",
  "auto": {
    "field_names": [
      "id"
    ],
    "seq": 0
  },
  "fields": {
    "id": {
      "type_code": "int"
    },
    "name": {
      "type_code": "string"
    }
  }
},
{
  "_id": {
    "$oid": "6495ce1c16abbbed0d78794a"
  },
  "name": "auth_group_permissions",
  "auto": {
    "field_names": [
      "id"
    ],
    "seq": 0
  },
  "fields": {
    "group_id": {
      "type_code": "int"
    },
    "id": {
      "type_code": "long"
    },
    "permission_id": {
      "type_code": "int"
    }
  }
},
{
  "_id": {
    "$oid": "6495ce1c16abbbed0d787950"
  },
  "name": "auth_user",
  "auto": {
    "field_names": [
      "id"
    ],
    "seq": 1
  },
  "fields": {
    "date_joined": {
      "type_code": "date"
    },
    "email": {
      "type_code": "string"
    },
    "first_name": {
      "type_code": "string"
    },
    "id": {
      "type_code": "int"
    },
    "is_active": {
      "type_code": "bool"
    },
    "is_staff": {
      "type_code": "bool"
    },
    "is_superuser": {
      "type_code": "bool"
    },
    "last_login": {
      "type_code": "date"
    },
    "last_name": {
      "type_code": "string"
    },
    "password": {
      "type_code": "string"
    },
    "username": {
      "type_code": "string"
    }
  }
},
{
  "_id": {
    "$oid": "6495ce1c16abbbed0d787955"
  },
  "name": "auth_user_groups",
  "auto": {
    "field_names": [
      "id"
    ],
    "seq": 0
  },
  "fields": {
    "group_id": {
      "type_code": "int"
    },
    "id": {
      "type_code": "long"
    },
    "user_id": {
      "type_code": "int"
    }
  }
},
{
  "_id": {
    "$oid": "6495ce1d16abbbed0d78795a"
  },
  "name": "auth_user_user_permissions",
  "auto": {
    "field_names": [
      "id"
    ],
    "seq": 0
  },
  "fields": {
    "id": {
      "type_code": "long"
    },
    "permission_id": {
      "type_code": "int"
    },
    "user_id": {
      "type_code": "int"
    }
  }
},
{
  "_id": {
    "$oid": "6495ce1d16abbbed0d78796d"
  },
  "name": "django_admin_log",
  "auto": {
    "field_names": [
      "id"
    ],
    "seq": 0
  },
  "fields": {
    "action_flag": {
      "type_code": "int"
    },
    "action_time": {
      "type_code": "date"
    },
    "change_message": {
      "type_code": "string"
    },
    "content_type_id": {
      "type_code": "int"
    },
    "id": {
      "type_code": "int"
    },
    "object_id": {
      "type_code": "string"
    },
    "object_repr": {
      "type_code": "string"
    },
    "user_id": {
      "type_code": "int"
    }
  }
},
{
  "_id": {
    "$oid": "6495ce7a16abbbed0d7879d1"
  },
  "name": "django_session",
  "fields": {
    "expire_date": {
      "type_code": "date"
    },
    "session_data": {
      "type_code": "string"
    },
    "session_key": {
      "type_code": "string"
    }
  }
},
{
  "_id": {
    "$oid": "6495d16016abbbed0d787ca5"
  },
  "name": "productApi_products",
  "auto": {
    "field_names": [
      "id"
    ],
    "seq": 0
  },
  "fields": {
    "id": {
      "type_code": "long"
    },
    "name": {
      "type_code": "string"
    },
    "startDate": {
      "type_code": "date"
    }
  }
},
{
  "_id": {
    "$oid": "6495dcf916abbbed0d7885b0"
  },
  "name": "productApi_product",
  "auto": {
    "field_names": [
      "id",
      "id",
      "id",
      "id",
      "id",
      "id"
    ],
    "seq": 13
  },
  "fields": {
    "id": {
      "type_code": "int"
    },
    "location": {
      "type_code": "string"
    },
    "masterName": {
      "type_code": "string"
    },
    "methodology": {
      "type_code": "string"
    },
    "name": {
      "type_code": "string"
    },
    "ownerName": {
      "type_code": "string"
    },
    "startDate": {
      "type_code": "date"
    },
    "developers": {
      "type_code": "array"
    }
  }
},
{
  "_id": {
    "$oid": "6496159eee2ee1aaf6b29b0a"
  },
  "name": "productApi_developer",
  "auto": {
    "field_names": [
      "id"
    ],
    "seq": 0
  },
  "fields": {
    "email": {
      "type_code": "string"
    },
    "id": {
      "type_code": "long"
    },
    "name": {
      "type_code": "string"
    }
  }
},
{
  "_id": {
    "$oid": "6496159eee2ee1aaf6b29b13"
  },
  "name": "productApi_product_developers",
  "auto": {
    "field_names": [
      "id"
    ],
    "seq": 0
  },
  "fields": {
    "developer_id": {
      "type_code": "long"
    },
    "id": {
      "type_code": "long"
    },
    "product_id": {
      "type_code": "long"
    }
  }
}])