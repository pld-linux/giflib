Summary:	GIF-manipulation library
Summary(es):	Biblioteca de manipulaciСn de archivos GIF
Summary(pl):	Biblioteka do obrСbki plikСw GIF
Summary(pt_BR):	Biblioteca de manipulaГЦo de arquivos GIF
Summary(ru):	Библиотека для работы с GIF-файлами
Summary(uk):	Б╕бл╕отека для роботи з GIF-файлами
Name:		giflib
Version:	4.1.0
%define		so_ver	4.1.0
Release:	3
License:	X Consortium-like
Group:		Libraries
# not original URL, but working
Source0:	http://www.netsw.org/graphic/bitmap/formats/gif/giflib/%{name}-%{version}.tar.gz
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/libungif-man-pages.tar.bz2
Patch0:		%{name}-fixes-from-libungif.patch
URL:		http://prtr-13.ucsc.edu/~badger/software/libungif/giflib.shtml
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	netpbm-devel
BuildRequires:	urt-devel
Provides:	libungif.so.4
Provides:	libungif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libungif
Obsoletes:	libungif4

%description
GIF loading and saving shared library. This version uses LZW
compression (warning: patent/license issues in some countries).

%description -l es
Es una biblioteca compartida para carga y grabaciСn de archivos GIF.

%description -l pl
Biblioteki dynamiczne do kompresowania i dekompresowania plikСw w
formacie GIF. Ta wersja przy zapisie u©ywa konwersji LZW (uwaga: w
niektСrych krajach powoduje to problemy zwi╠zane z patentem i
konieczno╤ci╠ nabycia licencji).

%description -l pt_BR
Biblioteca compartilhada para carga e gravaГЦo de arquivos GIF.

%description -l ru
Библиотека для загрузки и сохранения GIF-файлов.

%description -l uk
Б╕бл╕отека для загрузки та збереження GIF-файл╕в.

%package devel
Summary:	GIF-manipulation library header files and documentation.
Summary(es):	Archivos de inclusiСn, bibliotecas para biblioteca de manipulaciСn de GIF
Summary(pl):	Pliki nagЁСwkowe oraz dokumentacja do formatu GIF
Summary(pt_BR):	Arquivos de inclusЦo, bibliotecas para biblioteca de manipulaГЦo de GIF
Summary(ru):	Хедеры, библиотеки и документация GIF-библиотеки
Summary(uk):	Хедери, б╕бл╕отеки та документац╕я GIF-б╕бл╕отеки
Group:		Development/Libraries
Requires:	%{name} = %{version}
Provides:	libungif-devel
Provides:	libungif.so
Obsoletes:	libungif-devel
Obsoletes:	libungif4-devel

%description devel
Libraries and headers needed for developing programs that use libgif
to load and save gif image files.

%description devel -l es
Archivos de inclusiСn, bibliotecas y documentaciСn para biblioteca de
manipulaciСn de GIF.

%description devel -l pl
Biblioteki i pliki nagЁСwkowe niezbЙdne przy kompilacji programСw
wykorzystuj╠cych libgif.

%description devel -l pt_BR
Arquivos de inclusЦo, bibliotecas para biblioteca de manipulaГЦo de
GIF.

%description devel -l ru
Хедеры и библиотеки, необходимые для разработки программ, использующих
%{pkg_name} для загрузки и сохранения изображений в формате GIF.

%description devel -l uk
Хедери та б╕бл╕отеки, необх╕дн╕ для розробки програм, що
використовують %{pkg_name} для загрузки та збереження зображень у
формат╕ GIF.

%package static
Summary:	GIF-manipulation static library.
Summary(pl):	Biblioteki statyczne do obrСbki plikСw GIF
Summary(pt_BR):	Bibliotecas estАticas para desenvolvimento com libungif
Summary(ru):	Статические библиотеки GIF-библиотеки
Summary(uk):	Статичн╕ б╕бл╕отеки GIF-б╕бл╕отеки
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Provides:	libungif-static
Obsoletes:	libungif-static

%description static
Static libraries needed for developing programs that use libgif to
load and save gif image files.

%description static -l pl
Biblioteki statyczne do obrСbki plikСw GIF.

%description static -l pt_BR
Bibliotecas estАticas para desenvolvimento com libgif.

%description static -l ru
Это отдельный пакет со статическими библиотеками, которые больше не
входят в libgif-devel.

%description static -l uk
Це окремий пакет з╕ статичними б╕бл╕отеками, що б╕льше не входять до
складу libgif-devel.

%package progs
Summary:	Programs for converting and transforming gif images
Summary(pl):	Programy do konwertowania plikСw w formacie GIF
Summary(ru):	Программы для конвертирования и обработки GIF-файлов
Summary(uk):	Програми для конвертування та обробки GIF-файл╕в
Group:		Applications/Graphics
Requires:	%{name} = %{version}
Provides:	libungif-progs
Obsoletes:	libungif-progs

%description progs
This package contains various programs for manipulating gif image
files.

%description progs -l pl
Ten pakiet zawiera rС©norodne programy obsЁuguj╠ce pliki w formacie
GIF.

%description progs -l ru
Этот пакет содержит различные программы для обработки GIF-файлов.

%description progs -l uk
Цей пакет м╕стить р╕зноман╕тн╕ програми для обробки GIF-файл╕в.

%prep
%setup -q
%patch -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
CFLAGS="%{rpmcflags} -fwritable-strings"; export CFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR="$RPM_BUILD_ROOT" install

ln -sf libgif.so.%{so_ver} $RPM_BUILD_ROOT%{_libdir}/libungif.so.%{so_ver}
ln -sf libgif.so.%{so_ver} $RPM_BUILD_ROOT%{_libdir}/libungif.so.4
ln -sf libgif.so.%{so_ver} $RPM_BUILD_ROOT%{_libdir}/libungif.so
ln -sf libgif.a $RPM_BUILD_ROOT%{_libdir}/libungif.a
ln -sf libgif.la $RPM_BUILD_ROOT%{_libdir}/libungif.la

install -d $RPM_BUILD_ROOT%{_mandir}
bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS COPYING ChangeLog NEWS PATENT_PROBLEMS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/libungif.so.4

%files devel
%defattr(644,root,root,755)
%doc doc/*.{txt,png} doc/{gif_lib,index,liberror}.html
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%doc doc/gif2* doc/gif[a-z]* doc/*2gif*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
