%global oname Pypubsub
%global modname %(echo %oname | tr [:upper:] [:lower:])

Summary:	A Python publish-subcribe library 
Name:		python-%{modname}
Version:	4.0.3
Release:	1
License:	BSD
Group:		Development/Python
URL:		https://github.com/schollii/%{modname}
Source0:	https://github.com/schollii/%{modname}/archive/v%{version}/%{modname}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(pytest) 
BuildRequires:	python3dist(setuptools)

%description
PyPubSub provides a publish-subscribe API to facilitate event-based or
message-based architecture in a single-process application. It is pure
Python and works on Python 3.3+. It is centered on the notion of a topic;
senders publish messages of a given topic, and listeners subscribe to
messages of a given topic, all inside the same process. The package also
supports a variety of advanced features that facilitate debugging and
maintaining topics and messages in larger desktop- or server-based
applications.


%files
%license src/pubsub/LICENSE_BSD_Simple.txt
%doc README.rst
%doc src/pubsub/RELEASE_NOTES.txt
%{python3_sitelib}/%{oname}*
%{python3_sitelib}/pubsub/

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%py3_build

%install
%py3_install

%check
pushd tests/suite
PYTHONPATH=%{buildroot}%{python3_sitelib} PYTHONDONTWRITEBYTECODE=1 py.test
popd

