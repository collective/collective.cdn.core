.. contents:: Table of Contents
   :depth: 2

CDN Support for Plone
****************************************

Overview
========
This package implements a very basic CDN support for Plone sites. Resources 
registered at the portal registries (Styles, Scripts and KSS) can be 
delivered by specialized servers on different hostnames.

Also this package implements an experimental approach to serving image 
content from a CDN. We plan to improve this feature in future releases.

You must add a provider package in order to use CDN Support!

Available provider packages are:

   * AlternateHostname - collective.cdn.alternatehostname
   * Coral Networks - collective.cdn.coral
   * MultipleHostnames - collective.cdn.multiplehostnames 

Requirements
=============

   * Plone 3.3.x (http://plone.org/products/plone)
   * Plone 4.0.x (http://plone.org/products/plone)
    
Installation
=============
    
To enable this product,on a buildout based installation:

    1. Edit your buildout.cfg and add ``collective.cdn.core``
       to the list of eggs to install ::

        [buildout]
        ...
        eggs = 
            collective.cdn.core
    

If another package depends on the collective.cdn.core egg or 
includes its zcml directly you do not need to specify anything in the 
buildout configuration: buildout will detect this automatically.

After updating the configuration you need to run the ''bin/buildout'',
which will take care of updating your system.

Go to the 'Site Setup' page in the Plone interface and click on the
'Add/Remove Products' link.

Choose the product (check its checkbox) and click the 'Install' button.

Uninstall -- This can be done from the same management screen, but only
if you installed it from the quick installer.

Note: You may have to empty your browser cache and save your resource 
registries in order to see the effects of the product installation.

Usage
============

CDN settings
----------------
After installing this package, go to the 'Site Setup' page in the 
Plone interface and click on the 'CDN Configuration' link.

In this page you can choose which registries will use the CDN settings 
by clicking the respective checkboxes.

Also you must choose a provider -- added by specific packages as 
collective.cdn.coral -- and then inform hostnames, port and a path to 
be used by the provider.

Basic example
--------------
The simplest configuration would be possible by installing the 
collective.cdn.alternatehostname, which will enable you to add a alias 
hostname to your site. 

This configuration allows you to add a alternate hostname as your CDN, 
for example, using the alias localhost for a site running on 127.0.0.1. 


Known Issues
==============
Serving javascripts resources from a server not on the same domain as  
the main site could break some Plone features as this would fail the 
`same origin policy for javascript <https://developer.mozilla.org/en/Same_origin_policy_for_JavaScript>`_.

Serving images from CDN still is considered a experimental feature as 
it only supports images which are referenced through the *tag* method 
of the Archetypes ImageField. We plan to support other content types 
in the future. 

Sponsoring
===========

Development of this product was sponsored by `Simples Consultoria 
<http://www.simplesconsultoria.com.br/>`_.


Credits
========

    * Simples Consultoria (products at simplesconsultoria dot com dot br) - 
      Implementation


