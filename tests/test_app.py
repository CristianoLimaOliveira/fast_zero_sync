from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    # client = TestClient(
    #    app
    # )  # Arrange (organização do teste. ps: ainda não é o teste)

    response = client.get(
        '/'
    )  # Act ("vai lá e requisita o '/' para mim"), ou seja, é a fase de ação,
    # literalmente o teste

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Olá Mundo!'}  # assert


def test_page_hello_world_deve_retornar_ok_e_pagina_ola_mundo(client):
    response = client.get('/hello_world')
    assert response.status_code == HTTPStatus.OK
    assert (
        response.text
        == """
    <html>
        <head>
            <title>Nosso olá mundo</title>
        </head>
        <body>
            <h1>Olá Mundo!</h1>
        </body>
    </html>"""
    )


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'email': 'test@test.com',
            'password': 'password',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'testusername',
        'email': 'test@test.com',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'testusername',
                'email': 'test@test.com',
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'testusername2',
            'email': 'test@test.com',
            'password': 'password',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'testusername2',
        'email': 'test@test.com',
    }


def test_update_user_exception_not_found(client):
    response = client.put(
        '/users/2',
        json={
            'username': 'testusername2',
            'email': 'test2@test2.com',
            'password': 'password2',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_read_user(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'testusername2',
        'email': 'test@test.com',
    }


def test_read_user_exception_not_found(client):
    response = client.get('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_exception_not_fount(client):
    response = client.delete('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
