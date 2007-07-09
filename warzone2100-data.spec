%define	oname	warzone2100
%define	name	%{oname}-data
%define	version	2.0.7
%define	release	1

Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Group:		Games/Strategy
Source0:	http://download.berlios.de/warzone/%{name}-%{version}.tar.bz2
Url:		http://wz2100.net/
Summary:	3D realtime strategy on a future Earth
License:	GPL
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

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_gamesdatadir}/%{oname}
cp -r data/* %{buildroot}%{_gamesdatadir}/%{oname}

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%{_gamesdatadir}/%{oname}
