=================================
Welcome to python-indeedbot v1.0.0
=================================

Updated 04 April 2023

.. image:: https://img.shields.io/pypi/v/python-binance.svg
    :target: https://pypi.python.org/pypi/python-binance

.. image:: https://img.shields.io/pypi/l/python-binance.svg
    :target: https://pypi.python.org/pypi/python-binance

.. image:: https://img.shields.io/travis/sammchardy/python-binance.svg
    :target: https://travis-ci.org/sammchardy/python-binance

.. image:: https://img.shields.io/coveralls/sammchardy/python-binance.svg
    :target: https://coveralls.io/github/sammchardy/python-binance

.. image:: https://img.shields.io/pypi/wheel/python-binance.svg
    :target: https://pypi.python.org/pypi/python-binance

.. image:: https://img.shields.io/pypi/pyversions/python-binance.svg 
    :target: https://pypi.python.org/pypi/python-binance
    
|

This is an unofficial Python wrapper for the `Binance exchange REST API v3 <https://binance-docs.github.io/apidocs/spot/en>`_. I am in no way affiliated with Binance, use at your own risk.

If you came here looking for the `Binance exchange <https://www.binance.com/?ref=10099792>`_ to purchase cryptocurrencies, then `go here <https://www.binance.com/?ref=10099792>`_.
If you want to automate interactions with Binance stick around.

If you're interested in Binance's new DEX Binance Chain see my `python-binance-chain library <https://github.com/sammchardy/python-binance-chain>`_

Source code
  https://github.com/MarquisTheCoder/python-indeedbot

Documentation
  https://python-binance.readthedocs.io/en/latest/

Bot Telegram
  https://t.me/python_indeedbot


Features
--------

- Bypassing Indeed login with inital manual authentication
- Makes mulitple job searches depending on configuration
- pagination friendly for an start and end position
- Handles the application process with common questions and answers
- Resume handling for the application process
- Emailed updates to for updates and success or failure

Upgrading to v1.0.0+
--------------------

The breaking changes include the migration from wapi to sapi endpoints which related to the
wallet endpoints detailed in the `Binance Docs <https://binance-docs.github.io/apidocs/spot/en/#wallet-endpoints>`_

The other breaking change is for websocket streams and the Depth Cache Manager which have been
converted to use Asynchronous Context Managers. See examples in the Async section below or view the
`websockets <https://python-binance.readthedocs.io/en/latest/websockets.html>`_ and
`depth cache <https://python-binance.readthedocs.io/en/latest/depth_cache.html>`_ docs.

Quick Start
-----------

`Register an account with Indeed <https://secure.indeed.com/auth?hl=en_US&co=US&continue=https%3A%2F%2Fwww.indeed.com%2F%3Ffrom%3Dgnav-util-homepage&tmpl=desktop&service=my&from=gnav-util-homepage&jsContinue=https%3A%2F%2Fwww.indeed.com%2F&empContinue=https%3A%2F%2Faccount.indeed.com%2Fmyaccess>`_. and make sure to verify email and phone number.

.. code:: bash

    pip install python-binance


Donate
------

If this library helped you out feel free to donate.

- ETH: 0xD7a7fDdCfA687073d7cC93E9E51829a727f9fE70
- LTC: LPC5vw9ajR1YndE1hYVeo3kJ9LdHjcRCUZ
- NEO: AVJB4ZgN7VgSUtArCt94y7ZYT6d5NDfpBo
- BTC: 1Dknp6L6oRZrHDECRedihPzx2sSfmvEBys
