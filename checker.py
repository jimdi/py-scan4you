import click
import requests

@click.command()
@click.option('--type', default='file', required=True, prompt='type of check',
              help='type of check may be file, url, or domain.\nfile - make virus check on file (default)\nurl - make virus check on\ndomain - make check in blacklist from domain/url/IP\nexploit - make check of Exploit Pack')
@click.option('--disableav', default='', required=False,
              help='disable some av for this check, full list of av you can see at:\nhttp://scan4you.net/version.php')
@click.option('--enableav', default='all', required=False,
              help='enable specifed av for this check (use \'all\' if you want to enable all av),\nfull list of av you can see at: http://scan4you.net/version.php')
@click.option('--link', default=None, required=False, help='add url to result page to the end of results')
@click.argument('filename', nargs=1, required=True)
def check(filename, type, disableav, enableav, link):
    _id = ""
    _token = ""
    _url = 'http://scan4you.net/remote.php'
    _format = 'json'
    # txt|json
    click.echo('trying to upload %s, %s!' % (filename, type))

    payload = {'id': _id, 'token': _token, 'av_disable': disableav, 'av_enabled': enableav, 'frmt': _format,
               'action': type}

    # if type == 'file':
    #     payload[type] = filename

    if link != None:
        payload['link'] = 1

    headers = {}

    files = {'uppload': (filename, open(filename, 'rb'), 'application/octet-stream', {'Expires': '0'})}

    r = requests.post(_url, headers=headers, data=payload, files=files)

    if r.status_code == requests.codes.ok:
        print(r.text)
    else:
        print('Upload failed! %s' % (r.text))

if __name__ == '__main__':
    check()
