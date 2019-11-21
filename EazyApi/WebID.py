from EazyApi import *


class WebID:
    @classmethod
    def points(cls, tag):
        url = endpoint + '/points'
        params = {
            'path': '\\\\' + server + f'\\{tag}'
        }
        resp = eazy_requests(url, params)
        return resp.json()['WebId']

    @classmethod
    def elements(cls, afdb, subpaths):
        url = endpoint + '/elements'
        subpath = '\\'.join(subpaths)
        params = {
            'path': '\\\\' + server + f'\\{afdb}\\{subpath}'
        }
        resp = eazy_requests(url, params)
        return resp.json()['WebId']

    @classmethod
    def assetdatabases(cls, afdb):
        url = endpoint + '/assetdatabases'
        params = {
            'path': '\\\\' + server + f'\\{afdb}'
        }
        resp = eazy_requests(url, params)
        return resp.json()['WebId']

    @classmethod
    def attributes(cls, afdb, subpaths, attribute):
        url = endpoint + '/attributes'
        subpath = '\\'.join(subpaths)
        params = {
            'path': '\\\\' + server + f'\\{afdb}\\{subpath}|{attribute}'
        }
        resp = eazy_requests(url, params)
        return resp.json()['WebId']

    @classmethod
    def assetservers(cls, assetservers=server):
        url = endpoint + '/assetservers'
        params = {
            'path': '\\\\' + assetservers
        }
        resp = eazy_requests(url, params)
        return resp.json()['WebId']

    @classmethod
    def assetservers(cls, assetservers=server):
        url = endpoint + '/assetservers'
        params = {
            'path': '\\\\' + assetservers
        }
        resp = eazy_requests(url, params)
        return resp.json()['WebId']


if __name__ == '__main__':
    print(WebID.assetdatabases('CL'))
    print(WebID.points('3QT-PI-101-PL'))
    print(WebID.elements('CL', ['CL', '8工位']))
    print(WebID.attributes('CL', ['CL', '8工位'], '1#取坯車超載'))
