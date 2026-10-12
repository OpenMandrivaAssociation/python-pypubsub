%global oname Pypubsub
%global modname %(echo %oname | tr [:upper:] [:lower:])

Summary:	A Python publish-subcribe library 
Name:		python-%{modname}
Version:	4.0.7
Release:	2
License:	BSD
Group:		Development/Python
URL:		https://github.com/schollii/%{modname}
Source0:	https://github.com/schollii/%{modname}/archive/v%{version}/%{modname}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)

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
%{python_sitelib}/pubsub/
%{python_sitelib}/contrib/
%{python_sitelib}/pypubsub-%{version}.dist-info

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n pypubsub-4.0.7
# Cooker has setuptools 84. The sdist still rejects it.
sed -i 's/setuptools>=68,<77/setuptools>=68/' pyproject.toml

%build
# The GitHub archive is not a git checkout, so setuptools_scm needs the version.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py3_build

%install
%py3_install

# pytest is still Python 3.14. The suite can come back once pytest is rebuilt.

