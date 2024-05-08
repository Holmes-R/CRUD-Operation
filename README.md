
# CRUD Operation

Create,Read,Upade,Delete Operation on database.

Simple-JWT for authentication and access only authorized persons.
For authentication two tokens are needed i)access token ii)refresh token.

Simple JWT provides a JSON Web Token authentication backend for the Django REST Framework.

## Requirements

- Python
- Django
- Django REST Framework
- Django REST Framework Simple-JWT
## API Reference

#### Read items

```http
  GET /read/
```

#### Update Items

```http
  POST /update/<str:pk>/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `pk`      | `string` | **Required**. Id of item to update |

#### Get Details

```http
  GET /details/<str:pk>/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `pk`      | `string` | **Required**. Id of item to fetch |

#### Delete Items

```http
  DELETE /delete/<str:pk>/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `pk`      | `string` | **Required**. Id of item to delete |

#### Authorized User

```http
  POST /user/
```
#### Get the Access Token

```http
  GET /api/token/
```

#### Get the Refresh Token

```http
  GET /api/token/refresh/
```

