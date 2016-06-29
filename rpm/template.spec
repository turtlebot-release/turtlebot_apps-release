Name:           ros-kinetic-turtlebot-rapps
Version:        2.3.6
Release:        0%{?dist}
Summary:        ROS turtlebot_rapps package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/turtlebot_rapps
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-compressed-image-transport
Requires:       ros-kinetic-kobuki-auto-docking
Requires:       ros-kinetic-robot-pose-publisher
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-topic-tools
Requires:       ros-kinetic-turtlebot-bringup
Requires:       ros-kinetic-turtlebot-follower
Requires:       ros-kinetic-turtlebot-navigation
Requires:       ros-kinetic-turtlebot-teleop
Requires:       ros-kinetic-warehouse-ros
Requires:       ros-kinetic-world-canvas-server
BuildRequires:  ros-kinetic-catkin

%description
The core set of turtlebot 'app manager' apps are defined in this package.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed Jun 29 2016 Daniel Stonier <stonier@rnd.yujinrobot.com> - 2.3.6-0
- Autogenerated by Bloom

* Tue Jun 28 2016 Daniel Stonier <stonier@rnd.yujinrobot.com> - 2.3.5-0
- Autogenerated by Bloom

