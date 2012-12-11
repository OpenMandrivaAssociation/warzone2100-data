%define	oname	warzone2100
%define	name	%{oname}-data
%define	version	2.3.9
%define	release	1

Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Group:		Games/Strategy
Source0:        http://downloads.sourceforge.net/project/warzone2100/releases/%{version}/warzone2100-%{version}.tar.gz
Url:		http://wz2100.net/
Summary:	Data files for warzone2100
License:	GPLv2+
Requires:	%{oname} >= %{version}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Upon entering the game you land from your transport and establish your base.
Here you conduct research, design and manufacture vehicles, build new
structures and prepare your plans of global conquest. If the game goes badly
you'll end up fighting last ditch battles here to defend your base from
enemy attacks.

Combat is frenetic, with extensive graphical effects and damage to the
terrain and buildings giving rise to flying shrapnel and boulders. Within
the game are many different structures and vehicles. From an initial Command
Centre, you then go on to build Resource Extractors to provide fuel for Power
Generators, which in turn supply energy to Factories, Research Facilities and
weapons emplacements to protect your base.

Features:
 * 400+ Technologies to research 
 * 2,000+ different units to design 
 * 3 Large campaign maps to conquer 
 * 24 Fast play mission maps for extra action 
 * Intelligence Display sets objectives dynamically 
 * Interactive message system 
 * Fast Play Interface graphically Based 
 * Quick Screen Navigation 
 * Fast Find System for units & structures 
 * Set Factories to constant production 
 * Automatically send each factory's units to where you want them 

The Warzone 2100 ReDev Project aims to continue the vision of Pumpkin studios
started in 1999 with the game Warzone 2100, Which was closed source until
Dec 6, 2004 when it was let out the doors for the first time under a
GPL license.

%prep
%setup -q -n %{oname}-%{version}

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_gamesdatadir}/%{oname}
cp -r data/* %{buildroot}%{_gamesdatadir}/%{oname}

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%{_gamesdatadir}/%{oname}


%changelog
* Mon Oct 24 2011 Zombie Ryushu <ryushu@mandriva.org> 2.3.9-1
+ Revision: 705896
- Upgrade to 2.3.9

* Tue May 17 2011 Zombie Ryushu <ryushu@mandriva.org> 2.3.8-1
+ Revision: 675902
- Upgrade to 2.3.8

* Wed Jan 26 2011 Zombie Ryushu <ryushu@mandriva.org> 2.3.7-1
+ Revision: 632786
- Upgrade to 2.3.7

* Sat Dec 04 2010 Zombie Ryushu <ryushu@mandriva.org> 2.3.6-1mdv2011.0
+ Revision: 609552
+ rebuild (emptylog)

* Sun Sep 26 2010 Samuel Verschelde <stormi@mandriva.org> 2.3.5-1mdv2011.0
+ Revision: 581125
- update to 2.3.5

* Sat Aug 21 2010 Zombie Ryushu <ryushu@mandriva.org> 2.3.4-1mdv2011.0
+ Revision: 571589
- Upgrade to 2.3.4
- Upgrade to 2.3.4

* Wed Aug 04 2010 Funda Wang <fwang@mandriva.org> 2.3.3-1mdv2011.0
+ Revision: 565928
- New version 2.3.3

  + Zombie Ryushu <ryushu@mandriva.org>
    - Upgrade to 2.3.1a
    - Upgrade to 2.3.1a

* Sun Apr 25 2010 Funda Wang <fwang@mandriva.org> 2.3.0-1mdv2010.1
+ Revision: 538571
- New version 2.3.0

* Sat Nov 07 2009 Samuel Verschelde <stormi@mandriva.org> 2.2.4-1mdv2010.1
+ Revision: 462496
- videos are now in a separate package : warzone2100-videos-low
- new version 2.2.4
- added lo-res videos to the data, may split the package later

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 2.1.2-2mdv2010.0
+ Revision: 445736
- rebuild

* Sun Mar 08 2009 Emmanuel Andry <eandry@mandriva.org> 2.1.2-1mdv2009.1
+ Revision: 352993
- New version 2.1.2

* Wed Feb 11 2009 Zombie Ryushu <ryushu@mandriva.org> 2.1.1-1mdv2009.1
+ Revision: 339317
- Upgrade to 2.1.1 and include the music

* Mon Aug 25 2008 Emmanuel Andry <eandry@mandriva.org> 2.1-0.beta4.1mdv2009.0
+ Revision: 275749
- New version
- fix license
- fix source URL

* Sun Feb 03 2008 Emmanuel Andry <eandry@mandriva.org> 2.0.10-1mdv2008.1
+ Revision: 161734
- New version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Dec 15 2007 Emmanuel Andry <eandry@mandriva.org> 2.0.9-1mdv2008.1
+ Revision: 120386
- New version

* Mon Jul 09 2007 Funda Wang <fwang@mandriva.org> 2.0.7-1mdv2008.0
+ Revision: 50420
- New version

* Sun May 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.0.6-1mdv2008.0
+ Revision: 28846
- new version 2.0.6


* Wed Jan 17 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.0.5-1mdv2007.0
+ Revision: 109784
- update to 2.0.5 (fixes #28227)
  update url

  + Olivier Blin <oblin@mandriva.com>
    - Import warzone2100-data

* Tue Aug 29 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.0.4-1mdv2007.0
- 2.0.4

* Sat Sep 03 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.2.2-1mdk
- new data package to ease updates

